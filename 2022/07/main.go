package main

import (
	"fmt"
	"strings"

	"github.com/logan-connolly/aoc/internal/util"
)

const (
	DirectorySizeLimit = 100000
	FileSystemSize     = 70000000
	SpaceNeeded        = 30000000
)

func main() {
	lines := util.ReadInputAsStringLines("\n")

	p1 := partOne(lines)
	p2 := partTwo(lines)

	fmt.Printf("Solutions(p1=%d, p2=%d)", p1, p2)
}

func partOne(lines []string) int {
	fs := NewFileSystem()
	fs.Walk(lines)
	usage := fs.GetDiskUsage()

	var total int
	for path := range fs.mapping {
		if usage[path] <= DirectorySizeLimit {
			total += usage[path]
		}
	}
	return total
}

func partTwo(lines []string) int {
	fs := NewFileSystem()
	fs.Walk(lines)
	usage := fs.GetDiskUsage()
	threshold := SpaceNeeded - (FileSystemSize - usage["/"])

	currentBest := usage["/"]
	for path := range fs.mapping {
		if usage[path] < currentBest && usage[path] >= threshold {
			currentBest = usage[path]
		}
	}
	return currentBest
}

type File struct {
	name string
	size int
}

type Directory struct {
	path   string
	parent string
	files  []File
}

func NewDirectory(path string) Directory {
	tokens := strings.Split(path, "/")
	return Directory{
		path:   path,
		parent: "/" + strings.Join(tokens[1:len(tokens)-2], "/"),
	}
}

func (d *Directory) GetSize() int {
	var total int
	for _, file := range d.files {
		total += file.size
	}
	return total
}

type FileSystem struct {
	cwd     string
	mapping map[string]Directory
}

func NewFileSystem() FileSystem {
	mapping := make(map[string]Directory)
	mapping["/"] = Directory{path: "/", parent: ""}
	return FileSystem{cwd: "/", mapping: mapping}
}

func (fs *FileSystem) findNestedPaths(path string) []string {
	var nestedPaths []string
	for p := range fs.mapping {
		if strings.Contains(p, path) {
			nestedPaths = append(nestedPaths, p)
		}
	}
	return nestedPaths
}

func (fs *FileSystem) GetDiskUsage() map[string]int {
	usage := make(map[string]int)
	for dirPath := range fs.mapping {
		var totalSize int
		for _, nestedDirPath := range fs.findNestedPaths(dirPath) {
			d := fs.mapping[nestedDirPath]
			totalSize += d.GetSize()
		}
		usage[dirPath] = totalSize
	}
	return usage
}

func (fs *FileSystem) ChangeDirectory(target string) {
	if target == fs.cwd {
		return // no op
	} else if target == ".." {
		fs.cwd = fs.mapping[fs.cwd].parent
	} else {
		fs.cwd = fs.mapping[fs.cwd].path + target + "/"
	}
}

func (fs *FileSystem) AddDirectory(name string) {
	path := fs.cwd + name + "/"
	fs.mapping[path] = NewDirectory(path)
}

func (fs *FileSystem) AddFile(name string, size int) {
	d := fs.mapping[fs.cwd]
	d.files = append(d.files, File{name, size})
	fs.mapping[fs.cwd] = d
}

func (fs *FileSystem) Walk(lines []string) {
	for _, line := range lines {

		if strings.Contains(line, "$ ls") {
			continue
		}

		tokens := strings.Split(line, " ")

		switch line[:4] {
		case "$ cd":
			fs.ChangeDirectory(tokens[len(tokens)-1])
		case "dir ":
			fs.AddDirectory(tokens[len(tokens)-1])
		default:
			fs.AddFile(tokens[1], util.ToInt(tokens[0]))
		}
	}
}

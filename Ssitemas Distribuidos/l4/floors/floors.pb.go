// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v3.12.4
// source: floors/floors.proto

package floors

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type Start struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id int32 `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
}

func (x *Start) Reset() {
	*x = Start{}
	if protoimpl.UnsafeEnabled {
		mi := &file_floors_floors_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Start) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Start) ProtoMessage() {}

func (x *Start) ProtoReflect() protoreflect.Message {
	mi := &file_floors_floors_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Start.ProtoReflect.Descriptor instead.
func (*Start) Descriptor() ([]byte, []int) {
	return file_floors_floors_proto_rawDescGZIP(), []int{0}
}

func (x *Start) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

type ReadyRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id      int32 `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	IsReady bool  `protobuf:"varint,2,opt,name=is_ready,json=isReady,proto3" json:"is_ready,omitempty"`
}

func (x *ReadyRequest) Reset() {
	*x = ReadyRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_floors_floors_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ReadyRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ReadyRequest) ProtoMessage() {}

func (x *ReadyRequest) ProtoReflect() protoreflect.Message {
	mi := &file_floors_floors_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ReadyRequest.ProtoReflect.Descriptor instead.
func (*ReadyRequest) Descriptor() ([]byte, []int) {
	return file_floors_floors_proto_rawDescGZIP(), []int{1}
}

func (x *ReadyRequest) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *ReadyRequest) GetIsReady() bool {
	if x != nil {
		return x.IsReady
	}
	return false
}

type ReadyAnswer struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Continue bool `protobuf:"varint,2,opt,name=continue,proto3" json:"continue,omitempty"`
}

func (x *ReadyAnswer) Reset() {
	*x = ReadyAnswer{}
	if protoimpl.UnsafeEnabled {
		mi := &file_floors_floors_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ReadyAnswer) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ReadyAnswer) ProtoMessage() {}

func (x *ReadyAnswer) ProtoReflect() protoreflect.Message {
	mi := &file_floors_floors_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ReadyAnswer.ProtoReflect.Descriptor instead.
func (*ReadyAnswer) Descriptor() ([]byte, []int) {
	return file_floors_floors_proto_rawDescGZIP(), []int{2}
}

func (x *ReadyAnswer) GetContinue() bool {
	if x != nil {
		return x.Continue
	}
	return false
}

type Floor1ResultsRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id             int32 `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	SelectedWeapon int32 `protobuf:"varint,2,opt,name=selected_weapon,json=selectedWeapon,proto3" json:"selected_weapon,omitempty"`
	RandNumber     int32 `protobuf:"varint,3,opt,name=rand_number,json=randNumber,proto3" json:"rand_number,omitempty"`
}

func (x *Floor1ResultsRequest) Reset() {
	*x = Floor1ResultsRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_floors_floors_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Floor1ResultsRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Floor1ResultsRequest) ProtoMessage() {}

func (x *Floor1ResultsRequest) ProtoReflect() protoreflect.Message {
	mi := &file_floors_floors_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Floor1ResultsRequest.ProtoReflect.Descriptor instead.
func (*Floor1ResultsRequest) Descriptor() ([]byte, []int) {
	return file_floors_floors_proto_rawDescGZIP(), []int{3}
}

func (x *Floor1ResultsRequest) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *Floor1ResultsRequest) GetSelectedWeapon() int32 {
	if x != nil {
		return x.SelectedWeapon
	}
	return 0
}

func (x *Floor1ResultsRequest) GetRandNumber() int32 {
	if x != nil {
		return x.RandNumber
	}
	return 0
}

type Floor1ResultsAnswer struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Message string `protobuf:"bytes,1,opt,name=message,proto3" json:"message,omitempty"`
	IsDead  bool   `protobuf:"varint,2,opt,name=is_dead,json=isDead,proto3" json:"is_dead,omitempty"`
}

func (x *Floor1ResultsAnswer) Reset() {
	*x = Floor1ResultsAnswer{}
	if protoimpl.UnsafeEnabled {
		mi := &file_floors_floors_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Floor1ResultsAnswer) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Floor1ResultsAnswer) ProtoMessage() {}

func (x *Floor1ResultsAnswer) ProtoReflect() protoreflect.Message {
	mi := &file_floors_floors_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Floor1ResultsAnswer.ProtoReflect.Descriptor instead.
func (*Floor1ResultsAnswer) Descriptor() ([]byte, []int) {
	return file_floors_floors_proto_rawDescGZIP(), []int{4}
}

func (x *Floor1ResultsAnswer) GetMessage() string {
	if x != nil {
		return x.Message
	}
	return ""
}

func (x *Floor1ResultsAnswer) GetIsDead() bool {
	if x != nil {
		return x.IsDead
	}
	return false
}

type Floor2PathRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id           int32 `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	SelectedPath int32 `protobuf:"varint,2,opt,name=selected_path,json=selectedPath,proto3" json:"selected_path,omitempty"`
}

func (x *Floor2PathRequest) Reset() {
	*x = Floor2PathRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_floors_floors_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Floor2PathRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Floor2PathRequest) ProtoMessage() {}

func (x *Floor2PathRequest) ProtoReflect() protoreflect.Message {
	mi := &file_floors_floors_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Floor2PathRequest.ProtoReflect.Descriptor instead.
func (*Floor2PathRequest) Descriptor() ([]byte, []int) {
	return file_floors_floors_proto_rawDescGZIP(), []int{5}
}

func (x *Floor2PathRequest) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *Floor2PathRequest) GetSelectedPath() int32 {
	if x != nil {
		return x.SelectedPath
	}
	return 0
}

type Floor2PathAnswer struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Message string `protobuf:"bytes,1,opt,name=message,proto3" json:"message,omitempty"`
	IsOut   bool   `protobuf:"varint,2,opt,name=is_out,json=isOut,proto3" json:"is_out,omitempty"`
}

func (x *Floor2PathAnswer) Reset() {
	*x = Floor2PathAnswer{}
	if protoimpl.UnsafeEnabled {
		mi := &file_floors_floors_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Floor2PathAnswer) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Floor2PathAnswer) ProtoMessage() {}

func (x *Floor2PathAnswer) ProtoReflect() protoreflect.Message {
	mi := &file_floors_floors_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Floor2PathAnswer.ProtoReflect.Descriptor instead.
func (*Floor2PathAnswer) Descriptor() ([]byte, []int) {
	return file_floors_floors_proto_rawDescGZIP(), []int{6}
}

func (x *Floor2PathAnswer) GetMessage() string {
	if x != nil {
		return x.Message
	}
	return ""
}

func (x *Floor2PathAnswer) GetIsOut() bool {
	if x != nil {
		return x.IsOut
	}
	return false
}

type Floor3Try struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id         int32 `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	NTries     int32 `protobuf:"varint,2,opt,name=n_tries,json=nTries,proto3" json:"n_tries,omitempty"`
	NGoodTries int32 `protobuf:"varint,3,opt,name=n_good_tries,json=nGoodTries,proto3" json:"n_good_tries,omitempty"`
	RandNumber int32 `protobuf:"varint,4,opt,name=rand_number,json=randNumber,proto3" json:"rand_number,omitempty"`
}

func (x *Floor3Try) Reset() {
	*x = Floor3Try{}
	if protoimpl.UnsafeEnabled {
		mi := &file_floors_floors_proto_msgTypes[7]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Floor3Try) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Floor3Try) ProtoMessage() {}

func (x *Floor3Try) ProtoReflect() protoreflect.Message {
	mi := &file_floors_floors_proto_msgTypes[7]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Floor3Try.ProtoReflect.Descriptor instead.
func (*Floor3Try) Descriptor() ([]byte, []int) {
	return file_floors_floors_proto_rawDescGZIP(), []int{7}
}

func (x *Floor3Try) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *Floor3Try) GetNTries() int32 {
	if x != nil {
		return x.NTries
	}
	return 0
}

func (x *Floor3Try) GetNGoodTries() int32 {
	if x != nil {
		return x.NGoodTries
	}
	return 0
}

func (x *Floor3Try) GetRandNumber() int32 {
	if x != nil {
		return x.RandNumber
	}
	return 0
}

type Floor3ResultsRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id         int32 `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	NGoodTries int32 `protobuf:"varint,2,opt,name=n_good_tries,json=nGoodTries,proto3" json:"n_good_tries,omitempty"`
}

func (x *Floor3ResultsRequest) Reset() {
	*x = Floor3ResultsRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_floors_floors_proto_msgTypes[8]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Floor3ResultsRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Floor3ResultsRequest) ProtoMessage() {}

func (x *Floor3ResultsRequest) ProtoReflect() protoreflect.Message {
	mi := &file_floors_floors_proto_msgTypes[8]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Floor3ResultsRequest.ProtoReflect.Descriptor instead.
func (*Floor3ResultsRequest) Descriptor() ([]byte, []int) {
	return file_floors_floors_proto_rawDescGZIP(), []int{8}
}

func (x *Floor3ResultsRequest) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *Floor3ResultsRequest) GetNGoodTries() int32 {
	if x != nil {
		return x.NGoodTries
	}
	return 0
}

type Floor3ResultsAnswer struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Message string `protobuf:"bytes,1,opt,name=message,proto3" json:"message,omitempty"`
	IsDead  bool   `protobuf:"varint,2,opt,name=is_dead,json=isDead,proto3" json:"is_dead,omitempty"`
}

func (x *Floor3ResultsAnswer) Reset() {
	*x = Floor3ResultsAnswer{}
	if protoimpl.UnsafeEnabled {
		mi := &file_floors_floors_proto_msgTypes[9]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Floor3ResultsAnswer) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Floor3ResultsAnswer) ProtoMessage() {}

func (x *Floor3ResultsAnswer) ProtoReflect() protoreflect.Message {
	mi := &file_floors_floors_proto_msgTypes[9]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Floor3ResultsAnswer.ProtoReflect.Descriptor instead.
func (*Floor3ResultsAnswer) Descriptor() ([]byte, []int) {
	return file_floors_floors_proto_rawDescGZIP(), []int{9}
}

func (x *Floor3ResultsAnswer) GetMessage() string {
	if x != nil {
		return x.Message
	}
	return ""
}

func (x *Floor3ResultsAnswer) GetIsDead() bool {
	if x != nil {
		return x.IsDead
	}
	return false
}

var File_floors_floors_proto protoreflect.FileDescriptor

var file_floors_floors_proto_rawDesc = []byte{
	0x0a, 0x13, 0x66, 0x6c, 0x6f, 0x6f, 0x72, 0x73, 0x2f, 0x66, 0x6c, 0x6f, 0x6f, 0x72, 0x73, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x06, 0x66, 0x6c, 0x6f, 0x6f, 0x72, 0x73, 0x22, 0x17, 0x0a,
	0x05, 0x53, 0x74, 0x61, 0x72, 0x74, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x05, 0x52, 0x02, 0x69, 0x64, 0x22, 0x39, 0x0a, 0x0c, 0x52, 0x65, 0x61, 0x64, 0x79, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x05, 0x52, 0x02, 0x69, 0x64, 0x12, 0x19, 0x0a, 0x08, 0x69, 0x73, 0x5f, 0x72, 0x65, 0x61,
	0x64, 0x79, 0x18, 0x02, 0x20, 0x01, 0x28, 0x08, 0x52, 0x07, 0x69, 0x73, 0x52, 0x65, 0x61, 0x64,
	0x79, 0x22, 0x29, 0x0a, 0x0b, 0x52, 0x65, 0x61, 0x64, 0x79, 0x41, 0x6e, 0x73, 0x77, 0x65, 0x72,
	0x12, 0x1a, 0x0a, 0x08, 0x63, 0x6f, 0x6e, 0x74, 0x69, 0x6e, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x08, 0x52, 0x08, 0x63, 0x6f, 0x6e, 0x74, 0x69, 0x6e, 0x75, 0x65, 0x22, 0x70, 0x0a, 0x14,
	0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x31, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x73, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05,
	0x52, 0x02, 0x69, 0x64, 0x12, 0x27, 0x0a, 0x0f, 0x73, 0x65, 0x6c, 0x65, 0x63, 0x74, 0x65, 0x64,
	0x5f, 0x77, 0x65, 0x61, 0x70, 0x6f, 0x6e, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0e, 0x73,
	0x65, 0x6c, 0x65, 0x63, 0x74, 0x65, 0x64, 0x57, 0x65, 0x61, 0x70, 0x6f, 0x6e, 0x12, 0x1f, 0x0a,
	0x0b, 0x72, 0x61, 0x6e, 0x64, 0x5f, 0x6e, 0x75, 0x6d, 0x62, 0x65, 0x72, 0x18, 0x03, 0x20, 0x01,
	0x28, 0x05, 0x52, 0x0a, 0x72, 0x61, 0x6e, 0x64, 0x4e, 0x75, 0x6d, 0x62, 0x65, 0x72, 0x22, 0x48,
	0x0a, 0x13, 0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x31, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x73, 0x41,
	0x6e, 0x73, 0x77, 0x65, 0x72, 0x12, 0x18, 0x0a, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x12,
	0x17, 0x0a, 0x07, 0x69, 0x73, 0x5f, 0x64, 0x65, 0x61, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x08,
	0x52, 0x06, 0x69, 0x73, 0x44, 0x65, 0x61, 0x64, 0x22, 0x48, 0x0a, 0x11, 0x46, 0x6c, 0x6f, 0x6f,
	0x72, 0x32, 0x50, 0x61, 0x74, 0x68, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x0e, 0x0a,
	0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x02, 0x69, 0x64, 0x12, 0x23, 0x0a,
	0x0d, 0x73, 0x65, 0x6c, 0x65, 0x63, 0x74, 0x65, 0x64, 0x5f, 0x70, 0x61, 0x74, 0x68, 0x18, 0x02,
	0x20, 0x01, 0x28, 0x05, 0x52, 0x0c, 0x73, 0x65, 0x6c, 0x65, 0x63, 0x74, 0x65, 0x64, 0x50, 0x61,
	0x74, 0x68, 0x22, 0x43, 0x0a, 0x10, 0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x32, 0x50, 0x61, 0x74, 0x68,
	0x41, 0x6e, 0x73, 0x77, 0x65, 0x72, 0x12, 0x18, 0x0a, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67,
	0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65,
	0x12, 0x15, 0x0a, 0x06, 0x69, 0x73, 0x5f, 0x6f, 0x75, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x08,
	0x52, 0x05, 0x69, 0x73, 0x4f, 0x75, 0x74, 0x22, 0x77, 0x0a, 0x09, 0x46, 0x6c, 0x6f, 0x6f, 0x72,
	0x33, 0x54, 0x72, 0x79, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05,
	0x52, 0x02, 0x69, 0x64, 0x12, 0x17, 0x0a, 0x07, 0x6e, 0x5f, 0x74, 0x72, 0x69, 0x65, 0x73, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x06, 0x6e, 0x54, 0x72, 0x69, 0x65, 0x73, 0x12, 0x20, 0x0a,
	0x0c, 0x6e, 0x5f, 0x67, 0x6f, 0x6f, 0x64, 0x5f, 0x74, 0x72, 0x69, 0x65, 0x73, 0x18, 0x03, 0x20,
	0x01, 0x28, 0x05, 0x52, 0x0a, 0x6e, 0x47, 0x6f, 0x6f, 0x64, 0x54, 0x72, 0x69, 0x65, 0x73, 0x12,
	0x1f, 0x0a, 0x0b, 0x72, 0x61, 0x6e, 0x64, 0x5f, 0x6e, 0x75, 0x6d, 0x62, 0x65, 0x72, 0x18, 0x04,
	0x20, 0x01, 0x28, 0x05, 0x52, 0x0a, 0x72, 0x61, 0x6e, 0x64, 0x4e, 0x75, 0x6d, 0x62, 0x65, 0x72,
	0x22, 0x48, 0x0a, 0x14, 0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x33, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74,
	0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x05, 0x52, 0x02, 0x69, 0x64, 0x12, 0x20, 0x0a, 0x0c, 0x6e, 0x5f, 0x67, 0x6f,
	0x6f, 0x64, 0x5f, 0x74, 0x72, 0x69, 0x65, 0x73, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0a,
	0x6e, 0x47, 0x6f, 0x6f, 0x64, 0x54, 0x72, 0x69, 0x65, 0x73, 0x22, 0x48, 0x0a, 0x13, 0x46, 0x6c,
	0x6f, 0x6f, 0x72, 0x33, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x73, 0x41, 0x6e, 0x73, 0x77, 0x65,
	0x72, 0x12, 0x18, 0x0a, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x12, 0x17, 0x0a, 0x07, 0x69,
	0x73, 0x5f, 0x64, 0x65, 0x61, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x08, 0x52, 0x06, 0x69, 0x73,
	0x44, 0x65, 0x61, 0x64, 0x32, 0x86, 0x03, 0x0a, 0x0d, 0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x73, 0x53,
	0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x2e, 0x0a, 0x0c, 0x53, 0x74, 0x61, 0x72, 0x74, 0x4d,
	0x69, 0x73, 0x73, 0x69, 0x6f, 0x6e, 0x12, 0x0d, 0x2e, 0x66, 0x6c, 0x6f, 0x6f, 0x72, 0x73, 0x2e,
	0x53, 0x74, 0x61, 0x72, 0x74, 0x1a, 0x0d, 0x2e, 0x66, 0x6c, 0x6f, 0x6f, 0x72, 0x73, 0x2e, 0x53,
	0x74, 0x61, 0x72, 0x74, 0x22, 0x00, 0x12, 0x3d, 0x0a, 0x0e, 0x4d, 0x65, 0x72, 0x63, 0x65, 0x6e,
	0x61, 0x72, 0x79, 0x52, 0x65, 0x61, 0x64, 0x79, 0x12, 0x14, 0x2e, 0x66, 0x6c, 0x6f, 0x6f, 0x72,
	0x73, 0x2e, 0x52, 0x65, 0x61, 0x64, 0x79, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x13,
	0x2e, 0x66, 0x6c, 0x6f, 0x6f, 0x72, 0x73, 0x2e, 0x52, 0x65, 0x61, 0x64, 0x79, 0x41, 0x6e, 0x73,
	0x77, 0x65, 0x72, 0x22, 0x00, 0x12, 0x45, 0x0a, 0x06, 0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x31, 0x12,
	0x1c, 0x2e, 0x66, 0x6c, 0x6f, 0x6f, 0x72, 0x73, 0x2e, 0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x31, 0x52,
	0x65, 0x73, 0x75, 0x6c, 0x74, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x1b, 0x2e,
	0x66, 0x6c, 0x6f, 0x6f, 0x72, 0x73, 0x2e, 0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x31, 0x52, 0x65, 0x73,
	0x75, 0x6c, 0x74, 0x73, 0x41, 0x6e, 0x73, 0x77, 0x65, 0x72, 0x22, 0x00, 0x12, 0x3f, 0x0a, 0x06,
	0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x32, 0x12, 0x19, 0x2e, 0x66, 0x6c, 0x6f, 0x6f, 0x72, 0x73, 0x2e,
	0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x32, 0x50, 0x61, 0x74, 0x68, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x1a, 0x18, 0x2e, 0x66, 0x6c, 0x6f, 0x6f, 0x72, 0x73, 0x2e, 0x46, 0x6c, 0x6f, 0x6f, 0x72,
	0x32, 0x50, 0x61, 0x74, 0x68, 0x41, 0x6e, 0x73, 0x77, 0x65, 0x72, 0x22, 0x00, 0x12, 0x30, 0x0a,
	0x06, 0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x33, 0x12, 0x11, 0x2e, 0x66, 0x6c, 0x6f, 0x6f, 0x72, 0x73,
	0x2e, 0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x33, 0x54, 0x72, 0x79, 0x1a, 0x11, 0x2e, 0x66, 0x6c, 0x6f,
	0x6f, 0x72, 0x73, 0x2e, 0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x33, 0x54, 0x72, 0x79, 0x22, 0x00, 0x12,
	0x4c, 0x0a, 0x0d, 0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x33, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x73,
	0x12, 0x1c, 0x2e, 0x66, 0x6c, 0x6f, 0x6f, 0x72, 0x73, 0x2e, 0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x33,
	0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x1b,
	0x2e, 0x66, 0x6c, 0x6f, 0x6f, 0x72, 0x73, 0x2e, 0x46, 0x6c, 0x6f, 0x6f, 0x72, 0x33, 0x52, 0x65,
	0x73, 0x75, 0x6c, 0x74, 0x73, 0x41, 0x6e, 0x73, 0x77, 0x65, 0x72, 0x22, 0x00, 0x42, 0x09, 0x5a,
	0x07, 0x66, 0x6c, 0x6f, 0x6f, 0x72, 0x73, 0x2f, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_floors_floors_proto_rawDescOnce sync.Once
	file_floors_floors_proto_rawDescData = file_floors_floors_proto_rawDesc
)

func file_floors_floors_proto_rawDescGZIP() []byte {
	file_floors_floors_proto_rawDescOnce.Do(func() {
		file_floors_floors_proto_rawDescData = protoimpl.X.CompressGZIP(file_floors_floors_proto_rawDescData)
	})
	return file_floors_floors_proto_rawDescData
}

var file_floors_floors_proto_msgTypes = make([]protoimpl.MessageInfo, 10)
var file_floors_floors_proto_goTypes = []interface{}{
	(*Start)(nil),                // 0: floors.Start
	(*ReadyRequest)(nil),         // 1: floors.ReadyRequest
	(*ReadyAnswer)(nil),          // 2: floors.ReadyAnswer
	(*Floor1ResultsRequest)(nil), // 3: floors.Floor1ResultsRequest
	(*Floor1ResultsAnswer)(nil),  // 4: floors.Floor1ResultsAnswer
	(*Floor2PathRequest)(nil),    // 5: floors.Floor2PathRequest
	(*Floor2PathAnswer)(nil),     // 6: floors.Floor2PathAnswer
	(*Floor3Try)(nil),            // 7: floors.Floor3Try
	(*Floor3ResultsRequest)(nil), // 8: floors.Floor3ResultsRequest
	(*Floor3ResultsAnswer)(nil),  // 9: floors.Floor3ResultsAnswer
}
var file_floors_floors_proto_depIdxs = []int32{
	0, // 0: floors.FloorsService.StartMission:input_type -> floors.Start
	1, // 1: floors.FloorsService.MercenaryReady:input_type -> floors.ReadyRequest
	3, // 2: floors.FloorsService.Floor1:input_type -> floors.Floor1ResultsRequest
	5, // 3: floors.FloorsService.Floor2:input_type -> floors.Floor2PathRequest
	7, // 4: floors.FloorsService.Floor3:input_type -> floors.Floor3Try
	8, // 5: floors.FloorsService.Floor3Results:input_type -> floors.Floor3ResultsRequest
	0, // 6: floors.FloorsService.StartMission:output_type -> floors.Start
	2, // 7: floors.FloorsService.MercenaryReady:output_type -> floors.ReadyAnswer
	4, // 8: floors.FloorsService.Floor1:output_type -> floors.Floor1ResultsAnswer
	6, // 9: floors.FloorsService.Floor2:output_type -> floors.Floor2PathAnswer
	7, // 10: floors.FloorsService.Floor3:output_type -> floors.Floor3Try
	9, // 11: floors.FloorsService.Floor3Results:output_type -> floors.Floor3ResultsAnswer
	6, // [6:12] is the sub-list for method output_type
	0, // [0:6] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_floors_floors_proto_init() }
func file_floors_floors_proto_init() {
	if File_floors_floors_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_floors_floors_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Start); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_floors_floors_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ReadyRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_floors_floors_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ReadyAnswer); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_floors_floors_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Floor1ResultsRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_floors_floors_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Floor1ResultsAnswer); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_floors_floors_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Floor2PathRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_floors_floors_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Floor2PathAnswer); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_floors_floors_proto_msgTypes[7].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Floor3Try); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_floors_floors_proto_msgTypes[8].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Floor3ResultsRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_floors_floors_proto_msgTypes[9].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Floor3ResultsAnswer); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_floors_floors_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   10,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_floors_floors_proto_goTypes,
		DependencyIndexes: file_floors_floors_proto_depIdxs,
		MessageInfos:      file_floors_floors_proto_msgTypes,
	}.Build()
	File_floors_floors_proto = out.File
	file_floors_floors_proto_rawDesc = nil
	file_floors_floors_proto_goTypes = nil
	file_floors_floors_proto_depIdxs = nil
}

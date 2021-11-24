def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[6]<=4:
		# {"feature": "Coupon", "instances": 20, "metric_value": 0.7219, "depth": 2}
		if obj[3]>1:
			# {"feature": "Bar", "instances": 17, "metric_value": 0.5226, "depth": 3}
			if obj[11]<=2.0:
				# {"feature": "Distance", "instances": 16, "metric_value": 0.3373, "depth": 4}
				if obj[15]<=2:
					return 'True'
				elif obj[15]>2:
					return 'False'
				else: return 'False'
			elif obj[11]>2.0:
				return 'False'
			else: return 'False'
		elif obj[3]<=1:
			# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[5]<=0:
				return 'False'
			elif obj[5]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]>4:
		return 'False'
	else: return 'False'

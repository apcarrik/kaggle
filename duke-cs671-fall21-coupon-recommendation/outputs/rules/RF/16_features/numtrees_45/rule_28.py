def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[11]<=0.0:
		# {"feature": "Weather", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[15]>1:
				return 'True'
			elif obj[15]<=1:
				# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=0:
					return 'True'
				elif obj[4]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>0:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[11]>0.0:
		# {"feature": "Age", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[6]>0:
			# {"feature": "Direction_same", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[14]<=0:
				return 'False'
			elif obj[14]>0:
				return 'True'
			else: return 'True'
		elif obj[6]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[3]>1:
		# {"feature": "Time", "instances": 16, "metric_value": 1.0, "depth": 2}
		if obj[2]<=1:
			# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[6]<=1:
					return 'False'
				elif obj[6]>1:
					return 'True'
				else: return 'True'
			elif obj[5]>0:
				return 'False'
			else: return 'False'
		elif obj[2]>1:
			# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[15]<=1:
				return 'True'
			elif obj[15]>1:
				# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=1:
		return 'False'
	else: return 'False'

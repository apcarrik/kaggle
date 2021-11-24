def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[8]>1:
		# {"feature": "Distance", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[14]>1:
			# {"feature": "Age", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[5]<=2:
				return 'False'
			elif obj[5]>2:
				# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=2:
						return 'True'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[14]<=1:
			# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]<=2:
						return 'False'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[8]<=1:
		return 'True'
	else: return 'True'

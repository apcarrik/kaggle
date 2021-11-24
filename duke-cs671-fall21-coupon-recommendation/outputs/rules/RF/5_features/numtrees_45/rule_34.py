def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]<=1.0:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Occupation", "instances": 12, "metric_value": 1.0, "depth": 3}
			if obj[2]<=11:
				# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[4]<=1:
						return 'False'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			elif obj[2]>11:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1:
						return 'False'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]>3:
			return 'False'
		else: return 'False'
	elif obj[3]>1.0:
		# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[0]>1:
			return 'True'
		elif obj[0]<=1:
			# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=4:
				return 'False'
			elif obj[2]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'

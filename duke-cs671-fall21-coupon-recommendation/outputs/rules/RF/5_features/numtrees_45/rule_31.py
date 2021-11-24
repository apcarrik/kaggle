def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]>0:
		# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[3]<=1.0:
			# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[2]<=7:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=1:
						return 'True'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				elif obj[2]>7:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>1.0:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[2]<=12:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]>1:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			elif obj[2]>12:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'

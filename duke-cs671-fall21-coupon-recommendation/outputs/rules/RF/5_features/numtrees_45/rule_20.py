def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[4]>1:
		# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[3]>0.0:
			# {"feature": "Occupation", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[2]>6:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[0]>0:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]<=6:
				return 'False'
			else: return 'False'
		elif obj[3]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[4]<=1:
		# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 2}
		if obj[3]<=1.0:
			return 'False'
		elif obj[3]>1.0:
			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

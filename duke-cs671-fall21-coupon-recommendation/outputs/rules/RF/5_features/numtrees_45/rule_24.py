def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]<=2.0:
		# {"feature": "Distance", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[4]>1:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[0]>1:
					# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[0]<=1:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>1:
						return 'False'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[4]<=1:
			return 'False'
		else: return 'False'
	elif obj[3]>2.0:
		return 'True'
	else: return 'True'

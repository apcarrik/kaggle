def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]<=2.0:
		# {"feature": "Occupation", "instances": 21, "metric_value": 0.9984, "depth": 2}
		if obj[2]<=9:
			# {"feature": "Distance", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[0]>0:
					# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>2:
				return 'True'
			else: return 'True'
		elif obj[2]>9:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[0]<=3:
				# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>3:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]>2.0:
		return 'True'
	else: return 'True'

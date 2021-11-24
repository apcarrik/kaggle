def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]<=1.0:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[2]>2:
			# {"feature": "Distance", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[0]>1:
					# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]<=1:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>2:
				return 'False'
			else: return 'False'
		elif obj[2]<=2:
			return 'True'
		else: return 'True'
	elif obj[3]>1.0:
		# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[2]<=7:
			return 'False'
		elif obj[2]>7:
			# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[4]>2:
				return 'True'
			elif obj[4]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

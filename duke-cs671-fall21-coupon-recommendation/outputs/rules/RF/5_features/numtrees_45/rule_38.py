def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]<=2.0:
		# {"feature": "Coupon", "instances": 21, "metric_value": 0.9984, "depth": 2}
		if obj[0]>1:
			# {"feature": "Distance", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[4]<=1:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[2]<=7:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[2]>7:
					return 'False'
				else: return 'False'
			elif obj[4]>1:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=2:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[2]<=7:
				# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=2:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]>7:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]>2.0:
		return 'False'
	else: return 'False'

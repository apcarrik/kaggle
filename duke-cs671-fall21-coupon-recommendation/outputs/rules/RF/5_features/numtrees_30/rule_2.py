def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[2]>0:
		# {"feature": "Distance", "instances": 32, "metric_value": 0.9972, "depth": 2}
		if obj[4]>1:
			# {"feature": "Coupon", "instances": 19, "metric_value": 0.9495, "depth": 3}
			if obj[0]<=3:
				# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[3]>1.0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]<=1.0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>3:
				# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1]>1:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]<=1:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[0]>1:
						return 'False'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[3]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=0:
		return 'True'
	else: return 'True'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[1]>1:
		# {"feature": "Education", "instances": 24, "metric_value": 0.9183, "depth": 2}
		if obj[2]>1:
			# {"feature": "Passanger", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[0]>0:
				# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[4]>-1.0:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[3]>7:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[3]<=7:
						# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=1:
							return 'True'
						elif obj[5]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=-1.0:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[4]<=1.0:
				return 'True'
			elif obj[4]>1.0:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>3:
						return 'False'
					elif obj[3]<=3:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'

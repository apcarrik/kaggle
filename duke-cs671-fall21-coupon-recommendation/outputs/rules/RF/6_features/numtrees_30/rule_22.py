def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[3]>4:
		# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Coupon", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[1]>1:
				# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[2]<=1:
					return 'True'
				elif obj[2]>1:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[0]>0:
						# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]<=1:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[5]>1:
					return 'False'
				elif obj[5]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>1.0:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[1]>3:
				return 'False'
			elif obj[1]<=3:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[3]<=4:
		return 'True'
	else: return 'True'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]>1:
		# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[4]>0.0:
			# {"feature": "Passanger", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[1]>0:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]>2:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=2:
						return 'False'
					elif obj[5]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[4]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[3]<=1:
		return 'True'
	else: return 'True'

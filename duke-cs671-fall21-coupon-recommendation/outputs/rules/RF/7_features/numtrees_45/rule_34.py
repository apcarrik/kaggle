def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]<=2:
		# {"feature": "Coupon", "instances": 16, "metric_value": 0.8113, "depth": 2}
		if obj[1]>0:
			# {"feature": "Passanger", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[6]<=1:
					return 'True'
				elif obj[6]>1:
					# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]>2:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=2.0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]<=2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]>2:
		# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 2}
		if obj[3]>5:
			return 'False'
		elif obj[3]<=5:
			return 'True'
		else: return 'True'
	else: return 'False'

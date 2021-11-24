def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[4]>0:
			# {"feature": "Passanger", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[6]>0.0:
					# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[5]<=2.0:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]>1:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>0:
								return 'True'
							elif obj[3]<=0:
								return 'False'
							else: return 'False'
						elif obj[1]<=1:
							return 'True'
						else: return 'True'
					elif obj[5]>2.0:
						return 'False'
					else: return 'False'
				elif obj[6]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 2}
		if obj[4]<=8:
			return 'False'
		elif obj[4]>8:
			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[3]<=1:
				return 'True'
			elif obj[3]>1:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=3:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[6]>0.0:
		# {"feature": "Occupation", "instances": 21, "metric_value": 0.9852, "depth": 2}
		if obj[4]<=10:
			# {"feature": "Time", "instances": 18, "metric_value": 0.9183, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[2]>1:
					# {"feature": "Distance", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[8]>1:
						# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[3]>0:
							# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[0]>1:
										return 'True'
									elif obj[0]<=1:
										return 'False'
									else: return 'False'
								elif obj[7]>0:
									return 'False'
								else: return 'False'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					elif obj[8]<=1:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[4]>10:
			return 'False'
		else: return 'False'
	elif obj[6]<=0.0:
		return 'True'
	else: return 'True'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[5]<=1.0:
		# {"feature": "Time", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[2]>0:
				# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]<=5:
							# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[8]>1:
								return 'True'
							elif obj[8]<=1:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]>0.0:
									return 'False'
								elif obj[6]<=0.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>5:
							return 'False'
						else: return 'False'
					elif obj[3]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[5]>1.0:
		# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	else: return 'True'
def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 22, "metric_value": 0.7732, "depth": 2}
		if obj[4]>4:
			# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[3]>0:
				# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[6]<=2.0:
					# {"feature": "Direction_same", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[7]<=0:
						# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[2]>1:
								return 'True'
							elif obj[2]<=1:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=1:
									return 'True'
								elif obj[1]>1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[5]>1.0:
							return 'False'
						else: return 'False'
					elif obj[7]>0:
						return 'True'
					else: return 'True'
				elif obj[6]>2.0:
					return 'False'
				else: return 'False'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		elif obj[4]<=4:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'

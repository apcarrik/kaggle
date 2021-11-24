def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[5]<=1.0:
		# {"feature": "Distance", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[7]<=2:
			# {"feature": "Direction_same", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Passanger", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[3]<=6:
						return 'True'
					elif obj[3]>6:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=2:
							return 'True'
						elif obj[1]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]>1:
					# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]<=6:
							# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[4]<=2.0:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]>0:
									return 'False'
								elif obj[2]<=0:
									return 'False'
								else: return 'False'
							elif obj[4]>2.0:
								return 'True'
							else: return 'True'
						elif obj[3]>6:
							return 'True'
						else: return 'True'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[6]>0:
				return 'False'
			else: return 'False'
		elif obj[7]>2:
			return 'False'
		else: return 'False'
	elif obj[5]>1.0:
		return 'True'
	else: return 'True'

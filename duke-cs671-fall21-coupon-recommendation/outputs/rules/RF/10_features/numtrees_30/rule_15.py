def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Coupon", "instances": 26, "metric_value": 0.9957, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[4]>2:
				# {"feature": "Passanger", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[0]>0:
					# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.971, "depth": 5}
					if obj[6]<=2.0:
						# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[7]<=1.0:
							# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[9]<=1:
								# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[3]<=3:
									return 'False'
								elif obj[3]>3:
									return 'True'
								else: return 'True'
							elif obj[9]>1:
								# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[3]>1:
									return 'True'
								elif obj[3]<=1:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=0:
										return 'False'
									elif obj[8]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[7]>1.0:
							return 'False'
						else: return 'False'
					elif obj[6]>2.0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]<=2:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'

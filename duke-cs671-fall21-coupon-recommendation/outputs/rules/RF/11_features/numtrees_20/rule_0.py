def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Direction_same", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[9]<=0:
		# {"feature": "Occupation", "instances": 40, "metric_value": 1.0, "depth": 2}
		if obj[5]<=19:
			# {"feature": "Time", "instances": 37, "metric_value": 0.9953, "depth": 3}
			if obj[1]>0:
				# {"feature": "Age", "instances": 32, "metric_value": 0.9972, "depth": 4}
				if obj[3]<=5:
					# {"feature": "Coupon", "instances": 28, "metric_value": 0.9963, "depth": 5}
					if obj[2]>1:
						# {"feature": "Education", "instances": 21, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9774, "depth": 7}
							if obj[7]>0.0:
								# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 8}
								if obj[8]<=2.0:
									# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 9}
									if obj[6]>0.0:
										return 'False'
									elif obj[6]<=0.0:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=3:
												return 'True'
											else: return 'True'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>2.0:
									return 'True'
								else: return 'True'
							elif obj[7]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[7]<=3.0:
							return 'False'
						elif obj[7]>3.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]>5:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[5]>19:
			return 'False'
		else: return 'False'
	elif obj[9]>0:
		return 'True'
	else: return 'True'

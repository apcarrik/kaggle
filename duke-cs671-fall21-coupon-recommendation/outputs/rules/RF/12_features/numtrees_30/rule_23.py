def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[5]<=2:
		# {"feature": "Coupon", "instances": 30, "metric_value": 0.9183, "depth": 2}
		if obj[2]>1:
			# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.8113, "depth": 3}
			if obj[9]>-1.0:
				# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.7554, "depth": 4}
				if obj[8]<=1.0:
					# {"feature": "Age", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=4:
						# {"feature": "Time", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Occupation", "instances": 12, "metric_value": 0.65, "depth": 7}
							if obj[6]>5:
								return 'True'
							elif obj[6]<=5:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[0]>1:
									# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[11]>1:
											return 'True'
										elif obj[11]<=1:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								elif obj[0]<=1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]>3:
							return 'False'
						else: return 'False'
					elif obj[4]>4:
						return 'False'
					else: return 'False'
				elif obj[8]>1.0:
					return 'True'
				else: return 'True'
			elif obj[9]<=-1.0:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[6]<=10:
				return 'False'
			elif obj[6]>10:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[5]>2:
		return 'False'
	else: return 'False'

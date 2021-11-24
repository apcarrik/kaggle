def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Children", "instances": 27, "metric_value": 0.9751, "depth": 2}
		if obj[5]<=0:
			# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.9928, "depth": 3}
			if obj[9]>0.0:
				# {"feature": "Age", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[4]<=4:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[2]>0:
						# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[10]>0.0:
							# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[12]<=1:
									# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=5:
										return 'True'
									elif obj[7]>5:
										# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6]>2:
											return 'True'
										elif obj[6]<=2:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[12]>1:
									return 'False'
								else: return 'False'
							elif obj[1]>2:
								return 'False'
							else: return 'False'
						elif obj[10]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[4]>4:
					return 'True'
				else: return 'True'
			elif obj[9]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[5]>0:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'

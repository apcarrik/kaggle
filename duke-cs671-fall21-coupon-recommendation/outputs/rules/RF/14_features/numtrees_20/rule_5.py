def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[10]>0.0:
		# {"feature": "Income", "instances": 42, "metric_value": 0.8926, "depth": 2}
		if obj[8]<=6:
			# {"feature": "Time", "instances": 34, "metric_value": 0.9597, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Age", "instances": 20, "metric_value": 0.9928, "depth": 4}
				if obj[4]>0:
					# {"feature": "Occupation", "instances": 17, "metric_value": 0.9367, "depth": 5}
					if obj[7]<=20:
						# {"feature": "Gender", "instances": 15, "metric_value": 0.8366, "depth": 6}
						if obj[3]>0:
							# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[2]>2:
								# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[6]>0:
									# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[13]<=2:
										return 'False'
									elif obj[13]>2:
										return 'True'
									else: return 'True'
								elif obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]<=2:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					elif obj[7]>20:
						return 'True'
					else: return 'True'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				# {"feature": "Occupation", "instances": 14, "metric_value": 0.5917, "depth": 4}
				if obj[7]<=22:
					# {"feature": "Children", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[5]<=0:
						return 'True'
					elif obj[5]>0:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[6]<=2:
							return 'True'
						elif obj[6]>2:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[7]>22:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]>6:
			return 'True'
		else: return 'True'
	elif obj[10]<=0.0:
		# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[6]<=3:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[7]>7:
				return 'False'
			elif obj[7]<=7:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=0:
					return 'False'
				elif obj[0]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]>3:
			return 'True'
		else: return 'True'
	else: return 'False'

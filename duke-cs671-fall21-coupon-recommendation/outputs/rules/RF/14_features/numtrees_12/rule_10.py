def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[2]>0:
		# {"feature": "Passanger", "instances": 71, "metric_value": 0.9477, "depth": 2}
		if obj[0]>0:
			# {"feature": "Children", "instances": 65, "metric_value": 0.971, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Age", "instances": 35, "metric_value": 0.9947, "depth": 4}
				if obj[4]<=4:
					# {"feature": "Bar", "instances": 32, "metric_value": 0.9745, "depth": 5}
					if obj[9]<=1.0:
						# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 6}
						if obj[7]>2:
							# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 7}
							if obj[6]<=2:
								return 'True'
							elif obj[6]>2:
								# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[10]<=1.0:
									return 'False'
								elif obj[10]>1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[7]<=2:
							# {"feature": "Income", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[8]<=6:
								return 'False'
							elif obj[8]>6:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]>0:
									return 'True'
								elif obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[9]>1.0:
						# {"feature": "Time", "instances": 15, "metric_value": 0.8366, "depth": 6}
						if obj[1]<=2:
							return 'False'
						elif obj[1]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]>4:
					return 'True'
				else: return 'True'
			elif obj[5]>0:
				# {"feature": "Education", "instances": 30, "metric_value": 0.7838, "depth": 4}
				if obj[6]>0:
					# {"feature": "Time", "instances": 23, "metric_value": 0.4262, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[7]<=13:
							# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[10]<=2.0:
								return 'True'
							elif obj[10]>2.0:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[7]>13:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]<=0:
					# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[10]<=1.0:
						return 'False'
					elif obj[10]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Age", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[4]>2:
			return 'False'
		elif obj[4]<=2:
			# {"feature": "Income", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[8]>3:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			elif obj[8]<=3:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[2]>0:
		# {"feature": "Time", "instances": 39, "metric_value": 0.9957, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 3}
			if obj[7]<=7:
				# {"feature": "Distance", "instances": 22, "metric_value": 0.976, "depth": 4}
				if obj[12]<=2:
					# {"feature": "Age", "instances": 18, "metric_value": 1.0, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Gender", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[9]<=1.0:
									return 'False'
								elif obj[9]>1.0:
									return 'True'
								else: return 'True'
							elif obj[6]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>2:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[6]<=2:
							return 'True'
						elif obj[6]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[12]>2:
					return 'True'
				else: return 'True'
			elif obj[7]>7:
				# {"feature": "Direction_same", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[11]<=0:
					return 'False'
				elif obj[11]>0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]>0:
						return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Time", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[1]<=3:
			return 'False'
		elif obj[1]>3:
			# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[4]>0:
				return 'True'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

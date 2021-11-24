def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Coupon", "instances": 33, "metric_value": 0.9183, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Time", "instances": 20, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				# {"feature": "Age", "instances": 17, "metric_value": 0.9774, "depth": 4}
				if obj[4]>0:
					# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[9]>-1.0:
						# {"feature": "Gender", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 7}
							if obj[6]<=7:
								return 'True'
							elif obj[6]>7:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]>0:
									# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]>2.0:
										return 'True'
									elif obj[7]<=2.0:
										return 'False'
									else: return 'False'
								elif obj[5]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]>0:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=2:
								return 'False'
							elif obj[6]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[9]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[8]<=2.0:
				return 'False'
			elif obj[8]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[8]<=2.0:
			# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[4]>0:
				return 'True'
			elif obj[4]<=0:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]>2.0:
			# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[7]>0.0:
				# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[7]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'

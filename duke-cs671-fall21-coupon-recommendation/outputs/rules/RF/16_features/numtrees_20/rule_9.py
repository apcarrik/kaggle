def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Bar", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[11]<=2.0:
		# {"feature": "Coupon", "instances": 44, "metric_value": 0.9985, "depth": 2}
		if obj[3]>0:
			# {"feature": "Time", "instances": 30, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Weather", "instances": 24, "metric_value": 0.9799, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Income", "instances": 22, "metric_value": 0.9457, "depth": 5}
					if obj[10]<=4:
						# {"feature": "Occupation", "instances": 14, "metric_value": 0.7496, "depth": 6}
						if obj[9]<=9:
							# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.4395, "depth": 7}
							if obj[12]>0.0:
								return 'True'
							elif obj[12]<=0.0:
								# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[9]>9:
							# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[12]<=1.0:
								return 'False'
							elif obj[12]>1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[10]>4:
						# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[8]>0:
							# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[15]<=2:
								return 'False'
							elif obj[15]>2:
								return 'True'
							else: return 'True'
						elif obj[8]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				return 'True'
			else: return 'True'
		elif obj[3]<=0:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[9]>1:
				# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[13]>-1.0:
					return 'False'
				elif obj[13]<=-1.0:
					# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[6]>1:
						return 'False'
					elif obj[6]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[9]<=1:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[11]>2.0:
		return 'True'
	else: return 'True'
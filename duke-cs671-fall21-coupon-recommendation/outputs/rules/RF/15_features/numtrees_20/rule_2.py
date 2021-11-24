def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Income", "instances": 37, "metric_value": 0.9953, "depth": 2}
		if obj[9]>2:
			# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.971, "depth": 3}
			if obj[12]>0.0:
				# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.994, "depth": 4}
				if obj[11]>0.0:
					# {"feature": "Education", "instances": 14, "metric_value": 0.8631, "depth": 5}
					if obj[7]>0:
						# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[1]>0:
							# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[5]<=3:
								# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[10]>-1.0:
									return 'True'
								elif obj[10]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[5]>3:
								return 'False'
							else: return 'False'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					elif obj[7]<=0:
						return 'True'
					else: return 'True'
				elif obj[11]<=0.0:
					# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[1]>1:
						return 'False'
					elif obj[1]<=1:
						# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[2]>3:
							return 'False'
						elif obj[2]<=3:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[12]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[9]<=2:
			# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[11]>0.0:
				return 'False'
			elif obj[11]<=0.0:
				# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Income", "instances": 14, "metric_value": 0.3712, "depth": 2}
		if obj[9]<=6:
			return 'True'
		elif obj[9]>6:
			# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[5]>1:
		# {"feature": "Bar", "instances": 37, "metric_value": 0.9569, "depth": 2}
		if obj[10]<=2.0:
			# {"feature": "Coupon", "instances": 34, "metric_value": 0.9082, "depth": 3}
			if obj[2]>1:
				# {"feature": "Passanger", "instances": 25, "metric_value": 0.9896, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.8997, "depth": 5}
					if obj[11]>1.0:
						# {"feature": "Time", "instances": 12, "metric_value": 1.0, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Income", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[9]<=5:
								# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[8]>6:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[12]>-1.0:
										return 'False'
									elif obj[12]<=-1.0:
										return 'True'
									else: return 'True'
								elif obj[8]<=6:
									return 'True'
								else: return 'True'
							elif obj[9]>5:
								return 'False'
							else: return 'False'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[11]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[8]<=9:
						return 'True'
					elif obj[8]>9:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		elif obj[10]>2.0:
			return 'True'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Income", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[9]<=2:
			# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=3:
					return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[9]>2:
			return 'True'
		else: return 'True'
	else: return 'True'

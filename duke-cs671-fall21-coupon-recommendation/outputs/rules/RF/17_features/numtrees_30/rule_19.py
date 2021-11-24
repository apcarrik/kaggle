def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[10]<=12:
		# {"feature": "Income", "instances": 29, "metric_value": 0.8498, "depth": 2}
		if obj[11]>0:
			# {"feature": "Bar", "instances": 23, "metric_value": 0.9321, "depth": 3}
			if obj[12]<=3.0:
				# {"feature": "Education", "instances": 22, "metric_value": 0.9024, "depth": 4}
				if obj[9]<=1:
					# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[3]<=3:
						return 'True'
					elif obj[3]>3:
						# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[13]<=2.0:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'True'
							else: return 'True'
						elif obj[13]>2.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[9]>1:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[14]<=1.0:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[0]>0:
							# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[3]>1:
								return 'False'
							elif obj[3]<=1:
								# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=0:
									return 'True'
								elif obj[1]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[14]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[12]>3.0:
				return 'False'
			else: return 'False'
		elif obj[11]<=0:
			return 'True'
		else: return 'True'
	elif obj[10]>12:
		return 'False'
	else: return 'False'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Income", "instances": 40, "metric_value": 1.0, "depth": 2}
		if obj[11]<=6:
			# {"feature": "Time", "instances": 35, "metric_value": 0.9852, "depth": 3}
			if obj[2]>1:
				# {"feature": "Coupon_validity", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Coffeehouse", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[13]<=2.0:
						# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[12]>0.0:
								# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]<=3:
									return 'False'
								elif obj[3]>3:
									return 'True'
								else: return 'True'
							elif obj[12]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[6]>2:
							return 'False'
						else: return 'False'
					elif obj[13]>2.0:
						return 'True'
					else: return 'True'
				elif obj[4]>0:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				# {"feature": "Occupation", "instances": 17, "metric_value": 0.6723, "depth": 4}
				if obj[10]>5:
					return 'False'
				elif obj[10]<=5:
					# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[6]<=2:
						return 'True'
					elif obj[6]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[11]>6:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		return 'True'
	else: return 'True'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[6]>0:
		# {"feature": "Occupation", "instances": 30, "metric_value": 0.9968, "depth": 2}
		if obj[10]<=12:
			# {"feature": "Coupon", "instances": 27, "metric_value": 0.9751, "depth": 3}
			if obj[3]>1:
				# {"feature": "Bar", "instances": 22, "metric_value": 1.0, "depth": 4}
				if obj[12]>0.0:
					# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[14]<=2.0:
						# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[13]>-1.0:
								return 'True'
							elif obj[13]<=-1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[14]>2.0:
						return 'True'
					else: return 'True'
				elif obj[12]<=0.0:
					# {"feature": "Income", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[11]>3:
						return 'True'
					elif obj[11]<=3:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[16]>1:
								return 'False'
							elif obj[16]<=1:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]<=1:
				return 'False'
			else: return 'False'
		elif obj[10]>12:
			return 'True'
		else: return 'True'
	elif obj[6]<=0:
		return 'True'
	else: return 'True'

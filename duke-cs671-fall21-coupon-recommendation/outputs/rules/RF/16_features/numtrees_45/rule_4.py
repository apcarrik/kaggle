def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]>0:
		# {"feature": "Weather", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[13]>0.0:
				# {"feature": "Income", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[10]<=4:
					# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[9]<=7:
						# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[3]<=2:
							return 'False'
						elif obj[3]>2:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[8]>0:
								return 'False'
							elif obj[8]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[9]>7:
						return 'True'
					else: return 'True'
				elif obj[10]>4:
					return 'True'
				else: return 'True'
			elif obj[13]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[1]>0:
			return 'True'
		else: return 'True'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'

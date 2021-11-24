def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[9]<=16:
		# {"feature": "Weather", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Education", "instances": 18, "metric_value": 0.65, "depth": 3}
			if obj[8]<=1:
				# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]>1:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>1:
							# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]>0:
								return 'False'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]<=1:
							return 'True'
						else: return 'True'
					elif obj[3]<=1:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[8]>1:
				return 'True'
			else: return 'True'
		elif obj[1]>1:
			return 'False'
		else: return 'False'
	elif obj[9]>16:
		return 'False'
	else: return 'False'

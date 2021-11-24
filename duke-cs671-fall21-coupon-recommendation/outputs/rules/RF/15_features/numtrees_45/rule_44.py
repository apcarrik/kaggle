def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[5]>1:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[2]>1:
			# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[11]>0.0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[8]>2:
					# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]<=0:
									return 'False'
								elif obj[4]>0:
									return 'True'
								else: return 'True'
							elif obj[3]>0:
								return 'False'
							else: return 'False'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[8]<=2:
					return 'True'
				else: return 'True'
			elif obj[11]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[5]<=1:
		return 'False'
	else: return 'False'

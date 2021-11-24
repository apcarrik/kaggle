def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coffeehouse", "instances": 27, "metric_value": 0.9911, "depth": 2}
		if obj[10]<=3.0:
			# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.9544, "depth": 3}
			if obj[11]>0.0:
				# {"feature": "Children", "instances": 22, "metric_value": 0.9024, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Coupon", "instances": 16, "metric_value": 0.9887, "depth": 5}
					if obj[2]>1:
						# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[7]>4:
							# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[4]>1:
								return 'True'
							elif obj[4]<=1:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]>0:
									return 'False'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[7]<=4:
							# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]>0:
								return 'False'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			elif obj[11]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[10]>3.0:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		return 'True'
	else: return 'True'

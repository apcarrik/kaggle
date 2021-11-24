def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[8]>1:
		# {"feature": "Distance", "instances": 29, "metric_value": 0.9991, "depth": 2}
		if obj[13]<=2:
			# {"feature": "Bar", "instances": 26, "metric_value": 0.9829, "depth": 3}
			if obj[9]<=2.0:
				# {"feature": "Age", "instances": 24, "metric_value": 0.9544, "depth": 4}
				if obj[4]>1:
					# {"feature": "Children", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[2]>0:
							# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[5]>0:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[11]<=1.0:
						return 'True'
					elif obj[11]>1.0:
						# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=3:
								return 'False'
							elif obj[6]>3:
								return 'True'
							else: return 'True'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[9]>2.0:
				return 'False'
			else: return 'False'
		elif obj[13]>2:
			return 'False'
		else: return 'False'
	elif obj[8]<=1:
		return 'False'
	else: return 'False'

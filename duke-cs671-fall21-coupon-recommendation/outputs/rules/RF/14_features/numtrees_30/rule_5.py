def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[10]>0.0:
		# {"feature": "Time", "instances": 27, "metric_value": 0.951, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.9984, "depth": 3}
			if obj[7]<=6:
				# {"feature": "Age", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Income", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[8]<=3:
						# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[6]<=2:
							return 'True'
						elif obj[6]>2:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[8]>3:
						return 'False'
					else: return 'False'
				elif obj[4]>2:
					return 'True'
				else: return 'True'
			elif obj[7]>6:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>2:
						return 'True'
					elif obj[2]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[10]<=0.0:
		# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[6]<=3:
			return 'False'
		elif obj[6]>3:
			return 'True'
		else: return 'True'
	else: return 'False'

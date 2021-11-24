def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[7]<=9:
		# {"feature": "Coupon", "instances": 37, "metric_value": 0.9353, "depth": 2}
		if obj[2]>1:
			# {"feature": "Time", "instances": 28, "metric_value": 0.7496, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Age", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[4]<=3:
					# {"feature": "Income", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[8]<=5:
						# {"feature": "Children", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[5]<=0:
							return 'False'
						elif obj[5]>0:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>0:
								return 'False'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[8]>5:
						return 'True'
					else: return 'True'
				elif obj[4]>3:
					return 'True'
				else: return 'True'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[10]<=2.0:
				return 'False'
			elif obj[10]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[7]>9:
		# {"feature": "Income", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[8]<=3:
			return 'False'
		elif obj[8]>3:
			# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[6]>1:
					return 'False'
				elif obj[6]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'

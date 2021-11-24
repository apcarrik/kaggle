def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Children", "instances": 29, "metric_value": 0.9923, "depth": 2}
		if obj[5]>0:
			# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[10]<=1.0:
				# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=0:
						# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[2]>2:
							# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]<=3:
								return 'False'
							elif obj[4]>3:
								return 'True'
							else: return 'True'
						elif obj[2]<=2:
							return 'True'
						else: return 'True'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			elif obj[10]>1.0:
				return 'True'
			else: return 'True'
		elif obj[5]<=0:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[7]<=12:
					# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]>1:
							return 'False'
						elif obj[6]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[7]>12:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>1:
		return 'True'
	else: return 'True'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[4]>0:
		# {"feature": "Income", "instances": 45, "metric_value": 0.971, "depth": 2}
		if obj[8]>3:
			# {"feature": "Occupation", "instances": 27, "metric_value": 0.7642, "depth": 3}
			if obj[7]>4:
				# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[11]<=1.0:
					# {"feature": "Passanger", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[0]>1:
						# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[6]<=2:
							return 'True'
						elif obj[6]>2:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[0]<=1:
						# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[10]>0.0:
							return 'False'
						elif obj[10]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[11]>1.0:
					return 'True'
				else: return 'True'
			elif obj[7]<=4:
				return 'True'
			else: return 'True'
		elif obj[8]<=3:
			# {"feature": "Gender", "instances": 18, "metric_value": 0.9183, "depth": 3}
			if obj[3]>0:
				return 'False'
			elif obj[3]<=0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[7]<=9:
					return 'True'
				elif obj[7]>9:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]>0:
						return 'False'
					elif obj[6]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[4]<=0:
		return 'False'
	else: return 'False'

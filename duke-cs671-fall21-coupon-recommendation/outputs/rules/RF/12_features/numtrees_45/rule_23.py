def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[4]<=4:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[6]>9:
			# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[11]>1:
					return 'True'
				elif obj[11]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]<=9:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[2]>2:
				# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[5]>0:
					# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[9]<=1.0:
							return 'True'
						elif obj[9]>1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[4]>4:
		return 'True'
	else: return 'True'

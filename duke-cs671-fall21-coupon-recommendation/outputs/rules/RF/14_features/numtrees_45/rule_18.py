def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[4]>1:
		# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 2}
		if obj[7]>3:
			# {"feature": "Gender", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[3]<=0:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=0:
						return 'False'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]>0:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]<=3:
			return 'False'
		else: return 'False'
	elif obj[4]<=1:
		# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[7]>13:
				return 'True'
			elif obj[7]<=13:
				# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[10]>0.0:
					return 'False'
				elif obj[10]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	else: return 'True'

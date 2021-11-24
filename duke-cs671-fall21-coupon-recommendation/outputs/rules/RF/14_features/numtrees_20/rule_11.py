def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[2]>1:
		# {"feature": "Passanger", "instances": 33, "metric_value": 0.885, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Income", "instances": 23, "metric_value": 0.9656, "depth": 3}
			if obj[8]>3:
				# {"feature": "Distance", "instances": 14, "metric_value": 0.7496, "depth": 4}
				if obj[13]<=2:
					return 'True'
				elif obj[13]>2:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[8]<=3:
				# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[10]<=1.0:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				elif obj[10]>1.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[7]<=12:
				return 'True'
			elif obj[7]>12:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[9]<=1.0:
			# {"feature": "Income", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[8]<=3:
				# {"feature": "Time", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[1]>1:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[10]<=2.0:
							return 'True'
						elif obj[10]>2.0:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			elif obj[8]>3:
				return 'False'
			else: return 'False'
		elif obj[9]>1.0:
			# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[4]<=4:
				return 'True'
			elif obj[4]>4:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

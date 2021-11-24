def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Age", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[4]<=6:
			# {"feature": "Time", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Children", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[7]<=12:
						# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[9]>1.0:
							return 'False'
						elif obj[9]<=1.0:
							return 'True'
						else: return 'True'
					elif obj[7]>12:
						return 'True'
					else: return 'True'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[4]>6:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[7]<=20:
				return 'False'
			elif obj[7]>20:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>3:
		# {"feature": "Passanger", "instances": 15, "metric_value": 0.7219, "depth": 2}
		if obj[0]<=2:
			return 'False'
		elif obj[0]>2:
			# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

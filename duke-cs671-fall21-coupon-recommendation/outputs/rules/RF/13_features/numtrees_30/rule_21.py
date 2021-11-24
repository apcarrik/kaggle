def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[8]<=2.0:
		# {"feature": "Coupon", "instances": 30, "metric_value": 0.9968, "depth": 2}
		if obj[2]>2:
			# {"feature": "Occupation", "instances": 18, "metric_value": 0.9183, "depth": 3}
			if obj[7]<=9:
				# {"feature": "Distance", "instances": 14, "metric_value": 0.7496, "depth": 4}
				if obj[12]<=2:
					# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[10]>1.0:
						return 'True'
					elif obj[10]<=1.0:
						# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[1]>0:
							# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[12]>2:
					return 'False'
				else: return 'False'
			elif obj[7]>9:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=2:
			# {"feature": "Distance", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[12]>1:
				return 'False'
			elif obj[12]<=1:
				# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[4]>3:
					return 'True'
				elif obj[4]<=3:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[8]>2.0:
		return 'True'
	else: return 'True'

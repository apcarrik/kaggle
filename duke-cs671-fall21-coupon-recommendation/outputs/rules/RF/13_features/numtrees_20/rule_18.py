def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[7]<=7:
		# {"feature": "Time", "instances": 35, "metric_value": 0.8631, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Coupon", "instances": 28, "metric_value": 0.9403, "depth": 3}
			if obj[2]>1:
				# {"feature": "Gender", "instances": 21, "metric_value": 0.7919, "depth": 4}
				if obj[3]>0:
					# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.4138, "depth": 5}
					if obj[9]>0.0:
						return 'True'
					elif obj[9]<=0.0:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>2:
							return 'False'
						elif obj[4]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]<=0:
					# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[12]<=2:
							return 'True'
						elif obj[12]>2:
							return 'False'
						else: return 'False'
					elif obj[4]>2:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[10]>0.0:
							return 'False'
						elif obj[10]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=1:
				# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[9]<=1.0:
					return 'False'
				elif obj[9]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[7]>7:
		# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.8113, "depth": 2}
		if obj[9]>1.0:
			# {"feature": "Passanger", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		elif obj[9]<=1.0:
			return 'False'
		else: return 'False'
	else: return 'False'

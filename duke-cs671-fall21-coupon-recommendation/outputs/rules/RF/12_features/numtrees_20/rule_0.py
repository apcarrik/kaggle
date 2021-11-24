def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Education", "instances": 36, "metric_value": 0.9641, "depth": 2}
		if obj[5]>1:
			# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[8]>1.0:
				# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[7]<=1.0:
					# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=0:
							return 'True'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[7]>1.0:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]<=1.0:
				return 'False'
			else: return 'False'
		elif obj[5]<=1:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.9911, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Age", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[4]<=4:
					return 'True'
				elif obj[4]>4:
					# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]>5:
							return 'True'
						elif obj[6]<=5:
							return 'False'
						else: return 'False'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]>3:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[6]<=7:
					# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[7]<=0.0:
						# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[10]<=0:
							return 'False'
						elif obj[10]>0:
							return 'True'
						else: return 'True'
					elif obj[7]>0.0:
						return 'True'
					else: return 'True'
				elif obj[6]>7:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Gender", "instances": 15, "metric_value": 0.7219, "depth": 2}
		if obj[3]>0:
			return 'True'
		elif obj[3]<=0:
			# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[6]>3:
					return 'True'
				elif obj[6]<=3:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'

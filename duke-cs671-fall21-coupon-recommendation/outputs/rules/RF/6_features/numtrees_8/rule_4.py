def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Distance", "instances": 127, "metric_value": 0.9924, "depth": 1}
	if obj[5]<=2:
		# {"feature": "Coupon", "instances": 104, "metric_value": 0.9544, "depth": 2}
		if obj[1]>0:
			# {"feature": "Restaurant20to50", "instances": 91, "metric_value": 0.9254, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Occupation", "instances": 54, "metric_value": 0.9841, "depth": 4}
				if obj[3]<=14:
					# {"feature": "Passanger", "instances": 39, "metric_value": 0.9995, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Education", "instances": 25, "metric_value": 0.9896, "depth": 6}
						if obj[2]<=4:
							return 'False'
						elif obj[2]>4:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]>14:
					# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Passanger", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[0]<=2:
							return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]>1.0:
				# {"feature": "Occupation", "instances": 37, "metric_value": 0.7532, "depth": 4}
				if obj[3]<=12:
					# {"feature": "Passanger", "instances": 30, "metric_value": 0.5665, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Education", "instances": 18, "metric_value": 0.7642, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[3]>12:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Passanger", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]<=2:
						return 'False'
					elif obj[3]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=5:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						else: return 'True'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				elif obj[3]>5:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[5]>2:
		# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.7554, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Education", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[3]>0:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[0]<=1:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		elif obj[4]>1.0:
			return 'False'
		else: return 'False'
	else: return 'False'
